import React from 'react';


function processSubtitle(subtitle) {
    if (typeof subtitle == 'number') {
        console.log("Subtitle is a number");
        return "$" + subtitle.toLocaleString();
    }
    return subtitle;
};

const EVDetail = (props) => {
    return (
        <div className="ev-detail">
            <h3 className="ev-detail-title">{props.title}</h3>
            <p className="ev-detail-sub">{processSubtitle(props.subtitle)}</p>
        </div>
    )
};

export default EVDetail;