import React, { CSSProperties, useMemo, useRef, useState, ReactElement }  from "react";
import { DragDropProvider, DragOverEvent } from "@dnd-kit/react";
import { move }                            from "@dnd-kit/helpers";

import { SortableGroupProps } from "types";

/**A sortable group that allows its children to be sorted.*/
export default function SortableGroup( { 
        children = [],
        id,
        style    = {},
        setProps
    } : SortableGroupProps) {

    // At first render, we sort the children based on their index props
    // On later render, we do not sort because the sorting is handled by the itemsIDs array
    let initial_children = children

    initial_children = useMemo(() => [...children].sort((a, b) => {
        const indexA = (a as ReactElement).props._passedComponent.props.index ?? 0;
        const indexB = (b as ReactElement).props._passedComponent.props.index ?? 0;
        return indexA - indexB;
    }), [children]);

    // Store keys to order children
    const [itemIds, setItemIds] = useState<string[]>(
        initial_children.map(child => child.key)
    );

    // Reorder children IDs when dragging
    const handeDragOver = (event: DragOverEvent) => {
        
        setItemIds( (items) => move(items, event) );

        // Set sorted item IDs as a Dash props
        setProps({'sortedIds' : itemIds});

    };

    // Sort children based on the ordered keys
    const sortedChildren = itemIds.map(id => 
        initial_children.find(child => child.key === id)
    );

    return <DragDropProvider onDragOver={handeDragOver}>
        <div id = {id} style = {{...default_styles.div, ...style}}>
            {sortedChildren}
        </div>
    </DragDropProvider>
};

const default_styles : Record<string, CSSProperties> = {
    div : {
        flex         : 1,
        minHeight    : '200px',
        padding      : '16px',
        borderRadius : '8px',
        transition   : 'background-c    olor 0.2s'
    }
};