import React, { CSSProperties, ReactElement, useEffect } from "react";

import { useSortable }       from "@dnd-kit/react/sortable";
import { shapeIntersection } from '@dnd-kit/collision';

import { 
    RestrictToVerticalAxis,
    RestrictToHorizontalAxis 
} from "@dnd-kit/abstract/modifiers";

import { SortableItemProps } from "types";
import { HandleWrapper }     from "./HandleWrapper";
   
/**A sortable item used in a SortableGroup component.*/
export default function _SortableItem( { 
        children, 
        id, 
        className,
        index,
        styles,
        styles_drag,
        handle,
        restrict,
        lock                = false,
        handlePos           = 'start',
        transitionAnimation = {duration : 250, easing: 'ease', idle: true},
        setProps,
    } : SortableItemProps ) {

    const restrict_modifier = (
         restrict === 'vertical'   ? [RestrictToVerticalAxis]   :
        (restrict === 'horizontal' ? [RestrictToHorizontalAxis] : undefined)
    );

    const { ref, handleRef, isDragging } = useSortable({
        id, 
        index, 
        modifiers         : restrict_modifier,
        disabled          : lock,
        collisionDetector : shapeIntersection,
        transition        : (
            transitionAnimation === null ? 
            {duration : 0, idle: true} :
            transitionAnimation
        )
    });

    useEffect( () => {
        setProps({isDragging : isDragging})
    }, [isDragging]);

    // Style used when the item is locked
    let lock_styles = {
        handle : {cursor : lock ? 'default' : 'grab'},
        div    : {cursor : !lock && handle === undefined ? 'grab' : 'default'}
    } as Record<string, CSSProperties>;

    // Handle item defined by the user but wrapped with a forward ref to assign the handleRef
    let new_handle: ReactElement<typeof HandleWrapper> | null;

    if (handle !== undefined) {

        const handle_style = (
            isDragging ?
            {...lock_styles.handle, ...styles_drag?.handle} :
            {...lock_styles.handle, ...styles?.handle}
        )

        new_handle = <HandleWrapper 
            ref       = {handleRef} 
            className = 'sortable-item-handle'
            style     = {handle_style}
            child     = {handle} 
        />

    } else {
        new_handle = null
    };

    // Final div style applied to the div
    const div_style = (
        isDragging ? 
        {...default_styles.div, ...default_drag_styles.div, ...lock_styles.div, ...styles_drag?.div} : 
        {...default_styles.div, ...lock_styles.div, ...styles?.div}
    );

    return <div 
            id        = {id}
            className = {`sortable-item ${className || ''}`}
            ref       = {ref} 
            style     = {div_style}
        >
        {handlePos === 'start' ? new_handle : null}
        {children}
        {handlePos === 'end'   ? new_handle : null}
    </div>
};

// Default style applied to the element
const default_styles: Record<string, React.CSSProperties> = {
    div : {
        backgroundColor : 'light-dark(\
            var(--mantine-primary-color-1, white),\
            var(--mantine-color-dark-4, black))',
        border          : '1px solid black',
        padding         : '12px',
        margin          : '8px 0',
        borderRadius    : '4px',
        display         : 'flex',
        flex            : 1,
        alignItems      : 'center',
        gap             : '20px',
    }
};

// Default style applied on top of the default styles when the item is dragged
const default_drag_styles: Record<string, React.CSSProperties> = {
    div : {
        opacity : 0.5,
    }
};