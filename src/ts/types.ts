import { ReactElement, ReactNode } from "react";

/**Default properties for Dash components.*/
export interface DefaultComponentProps {

    /**Children of the component.*/
    children ?: ReactNode | ReactNode[] | null;

    /**Unique ID of the component.*/
    id ?: string;

    /**Class name of the component.*/
    className ?: string;

    /**CSS style to apply to the component.*/
    style ?: Record<string, any>;

    /**Function provided by Dash to setup properties usable in dash.Input and dash.Output.*/
    setProps : (props: Record<string, unknown>) => void;
};

/**A React element with a key property. This is a typical signature of Dash components.*/
interface ReactElementWithKey extends ReactElement {

    /**Key provided by Dash. This corresponds to the ID the user has provided.*/
    key : string;
};

/**Props for the SortableGroup component.*/
export interface SortableGroupProps extends Omit<DefaultComponentProps, 'children'> {
    
    /**Children passed as props. These should be SortableItem components.*/
    children ?: ReactElementWithKey[];
};

/**Props for the SortableItem component.*/
export interface SortableItemProps extends Omit<DefaultComponentProps, 'style' | 'id'> {

    /**Unique ID of the component.*/
    id : string;

    /**Initial position of the item in the sortable list.*/
    index : number;

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

    /**Whether to lock the item (i.e. make it not moveable) or not.*/
    lock      ?: boolean;

    /**Position of the handle either at the start or at the end of the row.*/
    handlePos ?: 'start' | 'end';

    /**
     * CSS styles to apply. 
     * This is a dictionary with keys 'div' and 'handle', each taking a dictionary with CSS properties.
    */
    styles    ?: {
        div    ?: Record<string, string>;
        handle ?: Record<string, string>;
    };
};

/**Props for the HandleWrapper component.*/
export interface HandleWrapperProps extends Omit<DefaultComponentProps, 'children' | 'setProps'> {

    /**Child component wrapped with a ref.*/
    child      : ReactNode;
};