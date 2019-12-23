import React from 'react';
import EVDetail from './EVDetail';

const EVCard = (props) => {
    return (
        <div className="box is-4 ev-card">
            {/* <h1 className="range">{props.ev.ranges[0]}</h1> */}
            <div className="column">
                <div className="row ev-card-header">
                    <div className="ev-image-container">
                        <img className="ev-image" src={process.env.PUBLIC_URL + 'media/model3.jpg'} alt="Model 3"></img>
                    </div>
                        <div className="range-container">
                            <h1 className="ev-range">310</h1>
                            <p className="range-subtitle">Range (miles)</p>
                        </div>
                </div>
                <div className="row ev-card-details">
                    <EVDetail
                        title="Brand"
                        subtitle={props.ev.brand}
                    />
                    <EVDetail
                        title="Make"
                        subtitle={props.ev.make}
                    />
                    <EVDetail
                        title="Price"
                        subtitle={props.ev.base_price}
                    />
                    <EVDetail
                        title="Price To Range Ratio"
                        // Determine the price to range ratio in this component
                        subtitle="$45 / 1 mile"
                    />
                </div>
                <p className="tip-text">Click for more details</p>
            </div>
            {/* <div><i class="fas fa-map-marked-alt"></i>{props.ev.ranges}</div> */}
        </div>
    )
};

export default EVCard;