import React, { forwardRef, cloneElement, isValidElement } from "react";

import { HandleWrapperProps } from "types";

/**Wrapper of the handle component provided by the user which adds the handleRef.*/
export const HandleWrapper = forwardRef<HTMLDivElement, HandleWrapperProps >(
    ({child, className, style}, ref) => {

        // React trick to force the re-rendering which happens when the style changes
        const styleKey = `${Date.now()}`;

        return <div 
            ref       = {ref} 
            className = {className} 
            style     = {{ display: 'contents' }}
        >
            {isValidElement(child) && cloneElement(
                child, 
                {
                    style : {...(child.props.style || {}), ...style}, 
                    key: styleKey})
                }
        </div>
    }
);