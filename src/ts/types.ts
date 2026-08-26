import { UniqueIdentifier }         from "@dnd-kit/core";
import { CSSProperties, ReactElement, ReactNode } from "react";

/**Default properties for Dash components.*/
export interface DefaultComponentProps {

    /**Children of the component.*/
    children ?: ReactNode | ReactNode[] | null;

    /**Unique ID of the component.*/
    id ?: string;

    /**CSS style to apply to the component.*/
    style ?: CSSProperties;

    /**Function provided by Dash to setup properties usable in dash.Input and dash.Output.*/
    setProps : (props: Record<string, unknown>) => void;
};

interface ReactElementWithKey extends ReactElement {

    /**Key provided by Dash. This corresponds to the ID the user has provided.*/
    key : string
};

export interface SortableGroupProps extends Omit<DefaultComponentProps, 'children'> {
    
    /**Children passed as props. These should be SortableItem components.*/
    children ?: ReactElementWithKey[];
};

export interface SortableItemProps extends Omit<DefaultComponentProps, 'id' | 'style'> {

    /**Unique ID for the item.*/
    id         : UniqueIdentifier;

    /**Initial position of the item in the sortable list.*/
    index      : number;

    /**
     * Whether to restrict items to vertical or horizontal motions only.
     * None means there is no restriction.
    */
    restrict  ?: 'vertical' | 'horizontal';

    /**
     * A Dash component used as handle to grab the row.
     * None means the entire row is draggable.
    */
    handle    ?: ReactNode;

    lock      ?: boolean;

    /**Position of the handle either at the start or at the end of the row.*/
    handlePos ?: 'start' | 'end';

    /**
     * CSS styles to apply. 
     * This is a dictionary with keys 'div' and 'handle', each taking a dictionary with CSS properties.
    */
    styles    ?: {
        div    ?: CSSProperties;
        handle ?: CSSProperties
    }
};

export interface HandleWrapperProps {

    /**Child component wrapped with a ref.*/
    child      : ReactNode;

    /**Class name.*/
    className ?: string;

    /**CSS style to apply to the child component.*/
    style     ?: CSSProperties;
};