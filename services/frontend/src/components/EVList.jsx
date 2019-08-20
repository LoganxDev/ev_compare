import React from 'react';

const EVList = (props) => {
    return (
        <div>
            {
                props.evs.map((ev) => {
                    return (
                        <h4
                            key={ev.id}
                            className="box title is-4"
                        >{ ev.brand }{ ev.make }
                        </h4>
                    )
                })
            }
        </div>
    )
};

export default EVList;