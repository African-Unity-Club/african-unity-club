import styled from 'styled-components'

export const InputSimpleStyled = styled.input`
    border: none;
    border-radius: .3rem;
    outline: none;
    padding: .3rem;
    font-size: 1rem;
    font-weight: 600;
    color: #1e1e1e;
    background-color: ${({ theme }) => theme};
    width: 100%;
    height: 2rem;
`

export const TextareaStyled = styled.textarea`
    border: none;
    border-radius: .3rem;
    outline: none;
    padding: .5rem;
    font-size: 1rem;
    font-weight: 600;
    color: #1e1e1e;
    background-color: ${({ theme }) => theme};
    width: 100%;
    height: 6rem;
    resize: none;
`