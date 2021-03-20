import styled, { css } from 'styled-components';

export const DropContainer = styled.div`
    margin: 2em 0 auto;
    padding: 4em 2em;
    border: 2px dashed #E14ECA;
    border-radius: 10px;
    text-align: center;

    ${props => props.isActive && css`
        border: 2px solid #E14ECA;
        color: #eee;
    `}

    &:focus,
    &:active {
        border: 2px solid #E14ECA;
        outline: none;
    }
`;

export const ParentContainer = styled.div`
    &:focus,
    &:active {
        border: none;
        outline: none;
    }
`;