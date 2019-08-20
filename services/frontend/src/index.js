import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import * as serviceWorker from './serviceWorker';
import axios from 'axios';

import EVList from './components/EVList';
// import AddEV from './components/AddEV';
import EVCards from './components/EVCards';

class App extends Component {
    constructor() {
        super();
        this.state = {
            evs: [],
            make: '',
            brand: '',
            base_price: 0,
            storage: 0,
        };
        // this.addEV = this.addEV.bind(this);
        this.handleChange = this.handleChange.bind(this);
    }

    componentDidMount() {
        this.getEvs();
    }

    getEvs() {
        axios.get(`${process.env.REACT_APP_EVS_SERVICE_URL}/evs`)
        .then((res) => {
            this.setState({ evs: res.data.data.evs });
        }).catch((err) => {
            console.log(err);
        });
    }

    // addEV(event) {
    //     event.preventDefault();
    //     const evData = {
    //         make: this.state.make,
    //         brand: this.state.brand,
    //         base_price: this.state.base_price,
    //         storage: this.state.storage
    //     }
    //     axios.post(`${process.env.REACT_APP_EVS_SERVICE_URL}/evs`, evData)
    //     .then((res) => {
    //         this.getEvs();
    //         this.setState({
    //             make: '',
    //             brand: '',
    //             base_price: 0,
    //             storage: 0,
    //         });
    //         console.log(res)
    //     })
    //     .catch((err) => {console.log(err)})
    // };

    handleChange(event) {
        const obj = {};
        obj[event.target.name] = event.target.value;
        this.setState(obj);
    }

    render() {
        return (
            <section className="section">
                <div className="container">
                    <div className="columns center">
                        <div className="column is-one-third">
                            <br />
                            <h1 className="title is-1">EV Compare</h1>
                            <br /><br />
                            <EVCards evs={this.state.evs}/>
                        </div>
                    </div>
                </div>
            </section>
        )
    }
};

ReactDOM.render(<App />, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
