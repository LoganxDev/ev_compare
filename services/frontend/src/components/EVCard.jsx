import React from 'react';

const EVCard = (props) => {
    return (
        <div className="box title is-4">
            <h2>{props.ev.brand} {props.ev.make}</h2>
            <div><i class="fas fa-map-marked-alt"></i>{props.ev.ranges}</div>
        </div>
    )
};

export default EVCard;