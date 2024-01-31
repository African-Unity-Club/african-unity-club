import styled from "styled-components";
import { Link } from "react-router-dom";


export const SpanLogoStyled = styled.span`
    display: flex;
    justify-content: center;
    align-items: center;
    width: 1.5rem;
    height: 1.5rem;
    border-radius: 50%;
    background: url(${props => props.logo}) no-repeat center center;
    background-size: cover;
`;

export const NetworkLinkStyled = styled(Link)`
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: .5rem;
    padding: .2rem .5rem .2rem .2rem;
    color: black;
    width: auto;
    border-radius: 1rem;
    border: 1px solid black;
    background-color: rgba(255, 0, 0, .2);
    cursor: pointer;
    transition: all .3s ease-in-out;
    &:hover {
        transform: scale(1.1);
    }
`;


export const Network = ({ network }) => {
    return (
        <NetworkLinkStyled to={`${network.link}`}>
            <SpanLogoStyled logo={network.logo} />
            <span className="net-name">{network.name}</span>
        </NetworkLinkStyled>
    );
}
