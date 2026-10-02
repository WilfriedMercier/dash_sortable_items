import React, { 
    CSSProperties,
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

import { 
    SortableGroupProps, 
    ReactElementWithKey 
} from "types";

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

    // Make sure children is an array
    children = Array.isArray(children) ? children : [children];
    children = children.map((child, index) => {
        return React.cloneElement(child, {index : index}) as ReactElementWithKey
    });

    const sortedChildrenRef = useRef<(ReactElementWithKey | undefined)[]>(children);
    const itemIdsRef        = useRef<string[]>(children.map(child => child.key));
    const isDraggingRef     = useRef<boolean>(false);
    const cancelRef         = useRef<boolean>(false);

    // Ref used to revert back the order if the action is canceled
    const originalIdsRef    = useRef<string[] | null>(null);

    // When children changes via a callback, we update the itemIds and set the sortedIds
    useEffect(() => {

        if (!isDraggingRef.current && !cancelRef.current) {

            sortedChildrenRef.current = children;

            // Save new order for the IDs
            itemIdsRef.current = children.map(child => child.key);
            
            setProps({ sortedIds: itemIdsRef.current });
            
        }

        cancelRef.current = false;

    }, [children]);

    const handleDragStart = (_: DragStartEvent) => {
        originalIdsRef.current = itemIdsRef.current;
        isDraggingRef.current  = true;
        cancelRef.current      = false;
    };

    // Reorder children IDs when dragging
    const handleDragOver = (event: DragOverEvent) => {

        const { source, target } = event.operation;
        if (!source || !target || source.id === target.id) return;

        itemIdsRef.current = move(itemIdsRef.current, event);
        
        setProps({ sortedIds : itemIdsRef.current });

        sortedChildrenRef.current = itemIdsRef.current.map(id => 
            children.find(child => child.key === id)
        );
    };

    // Commit or rollback when the drag finishes
    const handleDragEnd = (event: DragEndEvent) => {
        
        const { target, canceled } = event.operation;

        // Released with no droppable underneath (e.g. mouse drifted away
        // vertically), or drag was aborted (Esc) -> restore original order
        if ((canceled || !target) && (originalIdsRef.current != null)) {

            itemIdsRef.current = originalIdsRef.current;
            setProps( {sortedIds : originalIdsRef.current} );

            originalIdsRef.current = null;
            cancelRef.current      = true;

        }

        isDraggingRef.current = false;    
    };

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
            {sortedChildrenRef.current}
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