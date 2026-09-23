import React, { 
    CSSProperties, 
    useState, 
    useRef, 
    useEffect 
}  from "react";

import { Feedback } from "@dnd-kit/dom";
import { move }     from "@dnd-kit/helpers";
import { 
    DragDropProvider, 
    DragOverEvent, 
    DragEndEvent, 
    DragStartEvent
} from "@dnd-kit/react";

import { SortableGroupProps } from "types";

/**A sortable group that allows its children to be sorted.*/
export default function _SortableGroup( { 
        children = [],
        id,
        className,
        style         = {},
        showClone     = false,
        dropAnimation = {duration : 250, easing: 'ease'},
        setProps
    } : SortableGroupProps) {

    // Store keys to order children
    const [itemIds, setItemIds] = useState<string[]>(children.map(child => child.key));

    const originalIdsRef = useRef<string[]>(itemIds);
    useEffect( () => {originalIdsRef.current = itemIds}, [itemIds]);

    const handleDragStart = (_: DragStartEvent) => {
        originalIdsRef.current = itemIds;
    };

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
            setItemIds(originalIdsRef.current);
            setProps( {sortedIds : originalIdsRef.current} );
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
        children.find(child => child.key === id)
    );

    return <DragDropProvider 
            onDragStart = {handleDragStart}
            onDragOver  = {handleDragOver}
            onDragEnd   = {handleDragEnd}
            plugins     = {(defaults) => [
                ...defaults,
                Feedback.configure({
                    feedback      : showClone ? 'clone' : 'default',
                    dropAnimation : dropAnimation
                })
            ]}
        >
        <div 
            id        = {id}
            className = {`sortable-group ${className || ''}`}
            style     = {{...default_styles.div, ...style}}
        >
            {sortedChildren}
        </div>
    </DragDropProvider>
};

const default_styles : Record<string, CSSProperties> = {
    div : {
        display       : 'flex',
        flexDirection : 'column',
        flex          : 1,
        minHeight     : '200px',
        padding       : '16px',
        borderRadius  : '8px',
        transition    : 'background-color 0.2s',
        gap           : '16px'
    }
};