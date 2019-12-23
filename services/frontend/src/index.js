import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import * as serviceWorker from './serviceWorker';
import axios from 'axios';

import EVCards from './components/ev-containers/EVCards';
import ListNav from './components/layout/ListNav';
import Navbar from "./components/layout/Navbar";

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

    handleChange(event) {
        const obj = {};
        obj[event.target.name] = event.target.value;
        this.setState(obj);
    }

    render() {
        return (
            <div className="app">
                <Navbar />
                <section className="main-section">
                    <div className="container">
                        <ListNav />
                        <div className="columns center">
                            <div className="column is-two-thirds">
                                <EVCards evs={this.state.evs}/>
                            </div>
                        </div>
                    </div>
                </section>
            </div>
        )
    }
};

ReactDOM.render(<App />, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
