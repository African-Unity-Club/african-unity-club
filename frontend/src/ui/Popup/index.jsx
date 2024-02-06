import styled from 'styled-components'
import { InputComposeStyled } from "../InputCompose"
import { InputSimpleStyled, TextareaStyled } from "../Input";


const OverlayStyled = styled.div`
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    align-items: center;
    justify-content: center;

    .popup {
        background: #fff;
        padding: 2rem 1rem;
        border-radius: 5px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
        width: 320px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap: 1rem;
        position: relative;
    }

    h2 {
        font-size: 1.5rem;
        font-weight: bold;
        color: #1e1e1e;
    }

    .close-btn {
        cursor: pointer;
        position: absolute;
        top: 1rem;
        right: 1rem;
        font-size: .8rem;
        font-weight: bold;
        color: #1e1e1e;
        display: flex;
        align-items: center;
        justify-content: center;
        width: 1rem;
        height: 1rem;
        padding-bottom: .1rem;
        border-radius: 50%;
        background: crimson;
    }

    #formup {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap: 1.5rem;
        width: 100%;
    }

    .formup-body {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap: 1rem;
        width: 100%;
        color: #1e1e1e;
    }

    .formup-footer {
        display: flex;
        justify-content: space-between;
        align-items: center;
        width: 100%;

        button {
            padding: .5rem 1rem;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: .3s;
            font-weight: bold;
            background: #dae9f7;
        }
    }
`

export const PopupForm = ({ title, body }) => {

    // const OpenPopup = () => {
    //     document.querySelector('.overlay').style.display = 'flex'
    // }

    const ClosePopup = () => {
        document.querySelector('.overlay').style.display = 'none'
    }

    const handleSubmit = (e) => {
        e.preventDefault()
        document.getElementById('formup').addEventListener('submit', (e) => {
            e.preventDefault()
            let form = new FormData(e.target)
            let data = {}
            for (let [key, value] of form) {
                data[key] = value
            }
            console.log(data)
        })
        ClosePopup()
    }

    return (
        <OverlayStyled className='overlay'>
            <div class="popup">
                <span class="close-btn" onclick="closePopup()">&times;</span>
                <h2>{ title }</h2>
                
                <form id="formup" method='post' onSubmit={handleSubmit}>
                    <div className='formup-body'>{ body }</div>
                    <div className='formup-footer'>
                        <button type='reset'>Reset</button>
                        <button type='submit'>add</button>
                    </div>
                </form>
            </div>
        </OverlayStyled>
    )
}

