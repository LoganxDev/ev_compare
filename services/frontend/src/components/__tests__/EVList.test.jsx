import React from 'react';
import { shallow } from 'enzyme';
import renderer from 'react-test-renderer';

import EVList from '../EVList';

const evs = [
    {
        'make': 'Model 3',
        'brand': 'Tesla',
        'id': 1,
        'storage': 15
    },
    {
        'make': 'Model S',
        'brand': 'Tesla',
        'id': 2,
        'storage': 32
    }
];

test('EVList renders properly', () => {
    const wrapper = shallow(<EVList evs={evs} />);
    const element = wrapper.find('h4');
    expect(element.length).toBe(2);
    expect(element.get(0).props.children[0]).toBe('Tesla');
});

test('EVList renders a snapshot correctly', () => {
    const tree = renderer.create(<EVList evs={evs} />).toJSON();
    expect(tree).toMatchSnapshot();
});