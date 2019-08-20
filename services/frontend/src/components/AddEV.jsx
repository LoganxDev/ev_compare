import React from 'react';

const AddEV = (props) => {
    return (
        <form onSubmit={(event) => props.addEV(event)}>
            <div className="field">
                <input
                    name="make"
                    className="input is-large"
                    type="text"
                    placeholder="Enter vehicle make"
                    required
                    value={props.make}
                    onChange={props.handleChange}
                />
            </div>
            <div className="field">
                <input
                    name="brand"
                    className="input is-large"
                    type="text"
                    placeholder="Enter vehicle brand"
                    required
                    value={props.brand}
                    onChange={props.handleChange}
                />
            </div>
            <div className="field">
                <input
                    name="base_price"
                    className="input is-large"
                    type="text"
                    placeholder="Enter vehicle base price"
                    required
                    value={props.base_price}
                    onChange={props.handleChange}
                />
            </div>
            <div className="field">
                <input
                    name="storage"
                    className="input is-large"
                    type="text"
                    placeholder="Enter vehicle storage"
                    required
                    value={props.storage}
                    onChange={props.handleChange}
                />
            </div>
            <input
                type="submit"
                className="button is-primary is-large is-fullwidth"
                value="Submit"
            />
        </form>
    )
};

export default AddEV;