import React, { CSSProperties, ReactElement, useEffect } from "react";
import { useSortable } from "@dnd-kit/react/sortable";

import { 
    RestrictToVerticalAxis,
    RestrictToHorizontalAxis 
} from "@dnd-kit/abstract/modifiers";

import { SortableItemProps } from "types";
import { HandleWrapper }     from "./HandleWrapper";
   
/**A sortable item used in a SortableGroup component.*/
export default function SortableItem( { 
        children, 
        id, 
        index,
        styles,
        handle,
        restrict,
        lock      = false,
        handlePos = 'start',
        setProps,
    } : SortableItemProps ) {

    const restrict_modifier = (
         restrict === 'vertical'   ? [RestrictToVerticalAxis]   :
        (restrict === 'horizontal' ? [RestrictToHorizontalAxis] : undefined)
    );

    const { ref, handleRef, isDragging } = useSortable({
        id, 
        index, 
        modifiers : restrict_modifier,
        disabled  : lock
    });

    useEffect( () => {
        setProps({isDragging : isDragging})
    }, [isDragging]);

    // Style used to update the handle style dynamically
    let dynamic_styles = {
        handle : {cursor : lock ? 'default' : 'grab'},
        div    : {cursor : !lock && handle === undefined ? 'grab' : 'default'}
    } as Record<string, CSSProperties>;

    // Handle item defined by the user but wrapped with a forward ref to assign the handleRef
    let new_handle: ReactElement<typeof HandleWrapper> | null;
    if (handle !== undefined) {

        new_handle = <HandleWrapper 
            ref   = {handleRef} 
            style = {{...dynamic_styles.handle, ...styles?.handle}}
            child = {handle} 
        />

    } else {
        new_handle = null
    };

    return <div 
        id    = {id}
        ref   = {ref} 
        style = {{...default_styles.div, ...dynamic_styles.div, ...styles?.div}}
    >
        {handlePos === 'start' ? new_handle : null}
        {children}
        {handlePos === 'end'   ? new_handle : null}
    </div>
};

const default_styles: Record<string, React.CSSProperties> = {
    div : {
        backgroundColor : 'light-dark(\
            var(--mantine-primary-color-1, white),\
            var(--mantine-color-dark-4, black))',
        border          : '1px solid black',
        padding         : '12px',
        margin          : '8px 0',
        borderRadius    : '4px',
    }
};