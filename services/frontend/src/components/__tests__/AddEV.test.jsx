import React from 'react';
import { shallow } from 'enzyme';
import renderer from 'react-test-renderer';

import AddEV from '../AddEV';

test('AddEV renders properly', () => {
    const wrapper = shallow(<AddEV />);
    const element = wrapper.find('form');
    expect(element.find('input').length).toBe(5);
    expect(element.find('input').get(0).props.name).toBe('make');
    expect(element.find('input').get(1).props.name).toBe('brand');
    expect(element.find('input').get(2).props.name).toBe('base_price');
    expect(element.find('input').get(3).props.name).toBe('storage');
});

test('AddEV renders a  snapshot properly', () => {
   const tree = renderer.create(<AddEV />).toJSON();
   expect(tree).toMatchSnapshot(); 
});