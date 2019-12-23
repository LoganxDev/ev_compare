import React from 'react';

import EVCard from './EVCard';

const EVCards = (props) => {
    return (
        <div>
            {
                props.evs.map((ev) => {
                    return (
                        <EVCard
                            key={ev.id}
                            ev={ev}
                            className="no-shrink"
                        >
                        </EVCard>
                    )
                })
            }
        </div>
    )
};

export default EVCards;