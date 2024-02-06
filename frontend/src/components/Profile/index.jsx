import { InputComposeStyled } from "../../ui/InputCompose"
import { InputSimpleStyled, TextareaStyled } from "../../ui/Input";
import './index.css';
import { useParams } from "react-router-dom";
import nouser from '../../assets/nouser.png';
import { Skill } from '../../ui/Skill'
import { Exp } from '../../ui/Exp'
import { Network } from "../../ui/Network";
import { PencilSquare, Trash } from 'react-bootstrap-icons';
import { PopupForm } from "../../ui/Popup";


export default function Profil() {

    const { username } = useParams();

    const OpenPopup = (className) => {
        document.querySelector(`${className} .overlay`).style.display = 'flex'
    }

    const ClosePopup = () => {
        document.querySelector('.overlay').style.display = 'none'
    }

    const skillForm = (
        <>
            <InputComposeStyled>
                <label>Skill</label>
                <InputSimpleStyled  type="text" theme={"#dae9f7"}/>
            </InputComposeStyled>

            <InputComposeStyled>
                <label>Domain</label>
                <InputSimpleStyled  type="text" theme={"#dae9f7"}/>
            </InputComposeStyled>
            
            <TextareaStyled placeholder="description" theme={"#dae9f7"} />
        </>
    )

    const expForm = (
        <>
            <InputComposeStyled>
                <label>Title</label>
                <InputSimpleStyled  type="text" theme={"#dae9f7"}/>
            </InputComposeStyled>

            <TextareaStyled placeholder="description" theme={"#dae9f7"} />

            <InputComposeStyled>
                <label>Institution</label>
                <InputSimpleStyled  type="text" theme={"#dae9f7"}/>
            </InputComposeStyled>

            <InputComposeStyled>
                <label>Start Year</label>
                <InputSimpleStyled  type="year" theme={"#dae9f7"}/>
            </InputComposeStyled>

            <InputComposeStyled>
                <label>End Year</label>
                <InputSimpleStyled  type="year" theme={"#dae9f7"}/>
            </InputComposeStyled>
        </>
    )

    const awardForm = (
        <>
            <InputComposeStyled>
                <label>Title</label>
                <InputSimpleStyled  type="text" theme={"#dae9f7"}/>
            </InputComposeStyled>

            <TextareaStyled placeholder="description" theme={"#dae9f7"} />

            <InputComposeStyled>
                <label>Institution</label>
                <InputSimpleStyled  type="text" theme={"#dae9f7"}/>
            </InputComposeStyled>

            <InputComposeStyled>
                <label>Year</label>
                <InputSimpleStyled  type="year" theme={"#dae9f7"}/>
            </InputComposeStyled>
        </>
    )

    const networkForm = (
        <>
            <InputComposeStyled>
                <label>Network</label>
                <select >
                    <option value="" selected>-- choices --</option>
                    <option value="facebook">Facebook</option>
                    <option value="twitter">Twitter</option>
                    <option value="instagram">Instagram</option>
                    <option value="linkedin">Linkedin</option>
                    <option value="github">Github</option>
                    <option value="youtube">Youtube</option>
                    <option value="twitch">Twitch</option>
                    <option value="discord">Discord</option>
                    <option value="snapchat">Snapchat</option>
                    <option value="whatsapp">Whatsapp</option>
                    <option value="telegram">Telegram</option>
                </select>
            </InputComposeStyled>
            <InputComposeStyled>
                <label>Link</label>
                <InputSimpleStyled  type="url"  theme={"#dae9f7"}/>
            </InputComposeStyled>
        </>
    )


    return (
        <div className="Profil">
            <form className="profil-personal" method="post" onSubmit={``}>
                <h1>Personal Informations</h1>
                <div className="top">
                    <div className="left">

                        <InputComposeStyled>
                            <label>Username</label>
                            <InputSimpleStyled type="text"/>
                        </InputComposeStyled>

                        <InputComposeStyled>
                            <label>First Name</label>
                            <InputSimpleStyled  type="text"/>
                        </InputComposeStyled>

                        <InputComposeStyled>
                            <label>Last Name</label>
                            <InputSimpleStyled  type="text"/>
                        </InputComposeStyled>

                        <InputComposeStyled>
                            <label>Birth</label>
                            <InputSimpleStyled  type="text"/>
                        </InputComposeStyled>

                        <InputComposeStyled>
                            <label>Email</label>
                            <InputSimpleStyled  type="email"/>
                        </InputComposeStyled>

                        <InputComposeStyled>
                            <label>Phone</label>
                            <InputSimpleStyled  type="phone"/>
                        </InputComposeStyled>

                    </div>
                    <div className="right">
                        <img src={nouser} alt="avatar"/>
                        <button className="btn" type="button">Upload</button>
                    </div>
                </div>
                <div className="bottom">
                    <textarea placeholder="about"></textarea>
                    <button className="btn" type="submit">Save</button>
                </div>
            </form>

            <form className="profil-location" method="post" onSubmit={``}>
                <h1>Location</h1>
                <div className="top">
                    <div className="left">

                        <InputComposeStyled>
                            <label>Country</label>
                            <InputSimpleStyled  type="text"/>
                        </InputComposeStyled>

                        <InputComposeStyled>
                            <label>City</label>
                            <InputSimpleStyled  type="text"/>
                        </InputComposeStyled>

                        <InputComposeStyled>
                            <label>Language</label>
                            <InputSimpleStyled  type="text"/>
                        </InputComposeStyled>

                    </div>
                    <div className="right">

                        <InputComposeStyled>
                            <label>State</label>
                            <InputSimpleStyled  type="text"/>
                        </InputComposeStyled>

                        <InputComposeStyled>
                            <label>Street</label>
                            <InputSimpleStyled  type="text"/>
                        </InputComposeStyled>

                        <InputComposeStyled>
                            <label>TimeZone</label>
                            <InputSimpleStyled  type="text"/>
                        </InputComposeStyled>
                    </div>
                </div>
                <div className="bottom">
                    <button className="btn" type="submit">Save</button>
                </div>
            </form>

            <div className="profil-activity">
                <div className="skills">
                    <PopupForm title="New Skill" body={ skillForm } />
                    <div className="head">
                        <h1>Skills</h1>
                        <div className="bt">
                            <button className="btn" type="button" onClick={() => OpenPopup('.skills')}>
                                <PencilSquare size={16}/>
                            </button>
                            <button className="btn" type="button">
                                <Trash size={16}/>
                            </button>
                        </div>
                    </div>
                    <div className="body">
                        <Skill 
                            skill={
                                {
                                    name: 'title', 
                                    domain: 'technology',
                                    description: "Si vous avez plusieurs fichiers et composants, la vérification de ces points peut nécessiter une analyse plus approfondie de votre code. Si vous le souhaitez, vous pouvez partager le code du composant Social ainsi que les importations et utilisations associées, et je pourrai vous aider à identifier le problème spécifique."
                                }
                            }
                        />
                        <Skill 
                            skill={
                                {
                                    name: 'title', 
                                    domain: 'technology',
                                    description: "Si vous avez plusieurs fichiers et composants, la vérification de ces points peut nécessiter une analyse plus approfondie de votre code. Si vous le souhaitez, vous pouvez partager le code du composant Social ainsi que les importations et utilisations associées, et je pourrai vous aider à identifier le problème spécifique."
                                }
                            }
                        />
                        <Skill 
                            skill={
                                {
                                    name: 'title', 
                                    domain: 'technology',
                                    description: "Si vous avez plusieurs fichiers et composants, la vérification de ces points peut nécessiter une analyse plus approfondie de votre code. Si vous le souhaitez, vous pouvez partager le code du composant Social ainsi que les importations et utilisations associées, et je pourrai vous aider à identifier le problème spécifique."
                                }
                            }
                        />
                    </div>
                </div>
                <div className="experiences">
                    <PopupForm title="New Experience" body={ expForm } />
                    <div className="head">
                        <h1>Experiences</h1>
                        <div className="bt">
                            <button className="btn" type="button" onClick={() => OpenPopup('.experiences')}>
                                <PencilSquare size={16}/>
                            </button>
                            <button className="btn" type="button">
                                <Trash size={16}/>
                            </button>
                        </div>
                    </div>
                    <div className="body">
                        <Exp exp={
                            {
                                title: 'title',
                                description: "Si vous avez plusieurs fichiers et composants, la vérification de ces points peut nécessiter une analyse plus approfondie de votre code. Si vous le souhaitez, vous pouvez partager le code du composant Social ainsi que les importations et utilisations associées, et je pourrai vous aider à identifier le problème spécifique.",
                                institution: 'institution',
                                startYear: '2023-04-12',
                                endYear: 'today'
                            }} 
                        />

                        <Exp exp={
                            {
                                title: 'title',
                                description: "Si vous avez plusieurs fichiers et composants, la vérification de ces points peut nécessiter une analyse plus approfondie de votre code. Si vous le souhaitez, vous pouvez partager le code du composant Social ainsi que les importations et utilisations associées, et je pourrai vous aider à identifier le problème spécifique.",
                                institution: 'institution',
                                startYear: '2023-04-12',
                                endYear: 'today'
                            }} 
                        />

                        <Exp exp={
                            {
                                title: 'title',
                                description: "Si vous avez plusieurs fichiers et composants, la vérification de ces points peut nécessiter une analyse plus approfondie de votre code. Si vous le souhaitez, vous pouvez partager le code du composant Social ainsi que les importations et utilisations associées, et je pourrai vous aider à identifier le problème spécifique.",
                                institution: 'institution',
                                startYear: '2023-04-12',
                                endYear: 'today'
                            }} 
                        />
                    </div>
                </div>
                <div className="graduates">
                    <PopupForm title="New Graduate" body={ expForm } />
                    <div className="head">
                        <h1>Graduates & Certifications</h1>
                        <div className="bt">
                            <button className="btn" type="button" onClick={() => OpenPopup('.graduates')}>
                                <PencilSquare size={16}/>
                            </button>
                            <button className="btn" type="button">
                                <Trash size={16}/>
                            </button>
                        </div>
                    </div>
                    <div className="body">
                        <Exp exp={
                            {
                                title: 'title',
                                description: "Si vous avez plusieurs fichiers et composants, la vérification de ces points peut nécessiter une analyse plus approfondie de votre code. Si vous le souhaitez, vous pouvez partager le code du composant Social ainsi que les importations et utilisations associées, et je pourrai vous aider à identifier le problème spécifique.",
                                institution: 'institution',
                                startYear: '2023-04-12',
                                endYear: 'today'
                            }} 
                        />

                        <Exp exp={
                            {
                                title: 'title',
                                description: "Si vous avez plusieurs fichiers et composants, la vérification de ces points peut nécessiter une analyse plus approfondie de votre code. Si vous le souhaitez, vous pouvez partager le code du composant Social ainsi que les importations et utilisations associées, et je pourrai vous aider à identifier le problème spécifique.",
                                institution: 'institution',
                                startYear: '2023-04-12',
                                endYear: 'today'
                            }} 
                        />

                        <Exp exp={
                            {
                                title: 'title',
                                description: "Si vous avez plusieurs fichiers et composants, la vérification de ces points peut nécessiter une analyse plus approfondie de votre code. Si vous le souhaitez, vous pouvez partager le code du composant Social ainsi que les importations et utilisations associées, et je pourrai vous aider à identifier le problème spécifique.",
                                institution: 'institution',
                                startYear: '2023-04-12',
                                endYear: 'today'
                            }} 
                        />
                    </div>
                </div>
                <div className="awards">
                    <PopupForm title="New Award" body={ awardForm } />
                    <div className="head">
                        <h1>Awards</h1>
                        <div className="bt">
                            <button className="btn" type="button" onClick={() => OpenPopup('.awards')}>
                                <PencilSquare size={16}/>
                            </button>
                            <button className="btn" type="button">
                                <Trash size={16}/>
                            </button>
                        </div>
                    </div>
                    <div className="body">
                        <Exp exp={
                            {
                                title: 'title',
                                description: "Si vous avez plusieurs fichiers et composants, la vérification de ces points peut nécessiter une analyse plus approfondie de votre code. Si vous le souhaitez, vous pouvez partager le code du composant Social ainsi que les importations et utilisations associées, et je pourrai vous aider à identifier le problème spécifique.",
                                institution: 'institution',
                                startYear: '2023'
                            }} 
                        />

                        <Exp exp={
                            {
                                title: 'title',
                                description: "Si vous avez plusieurs fichiers et composants, la vérification de ces points peut nécessiter une analyse plus approfondie de votre code. Si vous le souhaitez, vous pouvez partager le code du composant Social ainsi que les importations et utilisations associées, et je pourrai vous aider à identifier le problème spécifique.",
                                institution: 'institution',
                                startYear: '2023'
                            }} 
                        />

                        <Exp exp={
                            {
                                title: 'title',
                                description: "Si vous avez plusieurs fichiers et composants, la vérification de ces points peut nécessiter une analyse plus approfondie de votre code. Si vous le souhaitez, vous pouvez partager le code du composant Social ainsi que les importations et utilisations associées, et je pourrai vous aider à identifier le problème spécifique.",
                                institution: 'institution',
                                startYear: '2023'
                            }} 
                        />
                    </div>
                </div>
                <div className="networks">
                    <PopupForm title="New Network" body={ networkForm } />
                    <div className="head">
                        <h1>Socials Network</h1>
                        <div className="bt">
                            <button className="btn" type="button" onClick={() => OpenPopup('.networks')}>
                                <PencilSquare size={16}/>
                            </button>
                            <button className="btn" type="button">
                                <Trash size={16}/>
                            </button>
                        </div>
                    </div>
                    <div className="body">
                        <Network network={
                            {
                                name: 'facebook',
                                link: 'https://facebook.com',
                                logo: nouser
                            }
                        }/>

                        <Network network={
                            {
                                name: 'facebook',
                                link: 'https://facebook.com',
                                logo: nouser
                            }
                        }/>

                        <Network network={
                            {
                                name: 'facebook',
                                link: 'https://facebook.com',
                                logo: nouser
                            }
                        }/>

                        <Network network={
                            {
                                name: 'facebook',
                                link: 'https://facebook.com',
                                logo: nouser
                            }
                        }/>
                    </div>
                </div>
            </div>

            <form method="post" onSubmit={`|`} className="experiences">
                <h1>Update Password</h1>
                <div className="top">
                    <div className="left">
                        <InputComposeStyled>
                            <label>Old password</label>
                            <InputSimpleStyled  type="password"/>
                        </InputComposeStyled>
                    </div>
                    <div className="right">
                        <InputComposeStyled>
                            <label>New password</label>
                            <InputSimpleStyled  type="password"/>
                        </InputComposeStyled>
                        <InputComposeStyled>
                            <label>confirm</label>
                            <InputSimpleStyled  type="password"/>
                        </InputComposeStyled>
                    </div>
                </div>
                <div className="bottom">
                    <button className="btn" type="submit">add</button>
                </div>
            </form>

            <form method="post" onSubmit={`|`} className="dbfactor">
                <h1>Double authentication factor</h1>
                <div className="left">
                    <span className="f-enable">
                        
                        <small>enable or disable</small>
                    </span>
                </div>
                <div className="rigth">
                    <img src="" alt="" />
                </div>
            </form>

        </div>
    )
}
