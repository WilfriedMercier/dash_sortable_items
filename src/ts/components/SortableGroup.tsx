import React, { CSSProperties, useMemo, useState, ReactElement }  from "react";

import { move } from "@dnd-kit/helpers";
import { 
    DragDropProvider, 
    DragOverEvent, 
    DragEndEvent, 
    DragStartEvent 
} from "@dnd-kit/react";

import { SortableGroupProps } from "types";

/**A sortable group that allows its children to be sorted.*/
export default function SortableGroup( { 
        children = [],
        id,
        className,
        style    = {},
        setProps
    } : SortableGroupProps) {

    // At first render, we sort the children based on their index props
    // On later render, we do not sort because the sorting is handled by the itemsIDs array
    let initial_children = children;

    initial_children = useMemo(() => [...children].sort((a, b) => {
        const indexA = (a as ReactElement).props._passedComponent.props.index ?? 0;
        const indexB = (b as ReactElement).props._passedComponent.props.index ?? 0;
        return indexA - indexB;
    }), [children]);

    // Store keys to order children
    const [itemIds, setItemIds] = useState<string[]>(
        initial_children.map(child => child.key)
    );

    // Ids used when to revert to original state when the Esc key is pressed during dragging
    const [originalIds, setOriginalIds] = useState<string[]>(itemIds);

    // Reorder children IDs when dragging
    const handleDragOver = (event: DragOverEvent) => {

        const { source, target } = event.operation;
        if (!source || !target || source.id === target.id) return;
        
        setItemIds( items => {
            const next = move(items, event);
            setProps({ sortedIds : next });
            return next;
        });
    };

    // Commit or rollback when the drag finishes
    const handleDragEnd = (event: DragEndEvent) => {
        
        const { target } = event.operation;

        // Released with no droppable underneath (e.g. mouse drifted away
        // vertically), or drag was aborted (Esc) -> restore original order
        if (event.canceled || !target) {
            setItemIds(originalIds);
            return;
        }

        setItemIds(items => {
            const next = move(items, event);
            setProps({ sortedIds: next });   // always send the NEW array
            return next;
        });
    };

    // Sort children based on the ordered keys
    const sortedChildren = itemIds.map(id => 
        initial_children.find(child => child.key === id)
    );

    return <DragDropProvider 
            onDragStart = {(_: DragStartEvent) => setOriginalIds(itemIds)}
            onDragOver  = {handleDragOver}
            onDragEnd   = {handleDragEnd}
        >
        <div 
            id        = {id} 
            className = {className}
            style     = {{...default_styles.div, ...style}}
        >
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