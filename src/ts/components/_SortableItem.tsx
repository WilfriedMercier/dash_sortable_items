import React, { CSSProperties, ReactElement, useEffect, ReactNode } from "react";

import { useSortable }       from "@dnd-kit/react/sortable";
import { shapeIntersection } from '@dnd-kit/collision';

import { 
    RestrictToVerticalAxis,
    RestrictToHorizontalAxis 
} from "@dnd-kit/abstract/modifiers";

import { SortableItemProps, handlePosType } from "types";
import { HandleWrapper }     from "./HandleWrapper";
   
/**A sortable item used in a SortableGroup component.*/
export default function _SortableItem( { 
        children, 
        id, 
        className,
        styles,
        stylesDrag,
        stylesDrop,
        stylesLock,
        handle,
        restrict,
        dynamicHandle,
        dynamicHandlePos,
        index               = 0,
        lock                = false,
        handlePos           = 'start',
        transitionAnimation = {duration : 250, easing: 'ease', idle: true},
        setProps,
    } : SortableItemProps ) {

    const restrict_modifier = (
         restrict === 'vertical'   ? [RestrictToVerticalAxis]   :
        (restrict === 'horizontal' ? [RestrictToHorizontalAxis] : undefined)
    );

    const { ref, handleRef, isDragging, isDropping } = useSortable({
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
        setProps({
            isDragging : isDragging
        })
    }, [isDragging]);

    useEffect( () => {
        setProps({
            isDropping : isDropping
        })
    }, [isDropping]);

    // Handle item defined by the user but wrapped with a forward ref to assign the handleRef
    let new_handle: ReactElement<typeof HandleWrapper> | null;
    let handle_pos_dynamic = handlePos;

    if (handle !== undefined) {

        // Dynamic style used for the handle if there is one
        let handle_style = default_styles?.handle;
        let handle_dynamic : ReactNode;

        if (isDragging) {
            handle_style       = {...handle_style, ...default_drag_styles?.handle, ...styles?.handle, ...stylesDrag?.handle};
            handle_dynamic     = dynamicHandle?.drag || handle;
            handle_pos_dynamic = dynamicHandlePos?.drag || handlePos;
        }
        else if (isDropping) {
            handle_style       = {...handle_style, ...default_drop_styles?.handle, ...styles?.handle, ...stylesDrop?.handle};
            handle_dynamic     = dynamicHandle?.drop || handle;
            handle_pos_dynamic = dynamicHandlePos?.drop || handlePos;
        }
        else if (lock) {
            handle_style       = {...handle_style, ...default_lock_styles?.handle, ...styles?.handle, ...stylesLock?.handle};
            handle_dynamic     = dynamicHandle?.lock || handle;
            handle_pos_dynamic = dynamicHandlePos?.lock || handlePos;
        }
        else {
            handle_style       = {...handle_style, ...styles?.handle};
            handle_dynamic     = handle;
            handle_pos_dynamic = handlePos;
        }

        new_handle = <HandleWrapper 
            ref       = {handleRef} 
            className = 'sortable-item-handle'
            style     = {handle_style}
            child     = {handle_dynamic} 
        />

    } else {
        new_handle = null;
    };

    // Dynamic style applied to the div element
    // If handle is provided, the cursor is set to default
    // Other dynamic styles are handled below
    let div_style = {
        ...default_styles?.div, 
        ...(handle !== undefined ? {cursor : 'default'} : {})
    };

    if (isDragging) {
        div_style = {...div_style, ...default_drag_styles?.div, ...styles?.div, ...stylesDrag?.div};
    }
    else if (isDropping) {
        div_style = {...div_style, ...default_drop_styles?.div, ...styles?.div, ...stylesDrop?.div};
    }
    else if (lock) {
        div_style = {...div_style, ...default_lock_styles?.div, ...styles?.div, ...stylesLock?.div};
    }
    else {
        div_style = {...div_style, ...styles?.div};
    }

    return <div 
            id        = {id}
            className = {`sortable-item ${className || ''}`}
            ref       = {ref} 
            style     = {div_style}
        >
        {handle_pos_dynamic === 'start' ? new_handle : null}
        {children}
        {handle_pos_dynamic === 'end'   ? new_handle : null}
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
        cursor          : 'grab'
    },
    handle : {
        cursor : 'grab'
    }
};

// Default style applied on top of the default styles when the item is dragged
const default_drag_styles: Record<string, React.CSSProperties> = {
    div : {
        opacity : 0.5,
    }
};

// Default style applied on top of the default styles when the item is dropped
const default_drop_styles: Record<string, React.CSSProperties> = {
    div : {
        opacity : 0.5,
    }
};

// Default style applied on top of the default styles when the item is locked
const default_lock_styles:  Record<string, CSSProperties> = {
    div : {
        cursor  : 'not-allowed',
        opacity : 0.5
    },
    handle : {
        cursor : 'not-allowed'
    }
};