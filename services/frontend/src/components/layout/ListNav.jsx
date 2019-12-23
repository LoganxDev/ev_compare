import React from 'react';

class ListNav extends React.Component {

    constructor() {
        super();
        this.state = {
            options: [
                {
                    id: 0,
                    text: "Range",
                    selected: true
                },
                {
                    id: 1,
                    text: "Price",
                    selected: false
                },
                {
                    id: 2,
                    text: "Price to Range",
                    selected: false
                }
            ]
        }
    }

    onClick() {

    }

    render() {
        const list = this.state.options;
        return (
            <div className="list-nav">
                <p className="sortby-label">Sort By: </p>
                <div className="dropdown is-hoverable">
                    <div className="dropdown-trigger">
                        <p aria-haspopup="true" aria-controls="dropdown-menu">
                        <span className="dropdown-active">Range</span>
                        <span className="icon is-small">
                            <i className="fas fa-angle-down" aria-hidden="true"></i>
                        </span>
                        </p>
                    </div>
                    <div className="dropdown-menu" id="dropdown-menu" role="menu">
                        <div className="dropdown-content">
                            {list.map((option) => (
                                <a className="dropdown-item" key={option.id}>
                                    {option.text}
                                </a>
                            ))}
                        </div>
                    </div>
                </div>
            </div>
        );
    }
};

export default ListNav;