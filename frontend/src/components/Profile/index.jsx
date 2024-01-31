import { InputComposeStyled } from "../../ui/InputCompose"
import { InputSimpleStyled } from "../../ui/Input";
import './index.css';
import { useParams } from "react-router-dom";
import nouser from '../../assets/nouser.png';
import { Skill } from '../../ui/Skill'
import { Exp } from '../../ui/Exp'


export default function Profil() {

    const { username } = useParams();

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
            
            <form className="skills" method="post" onSubmit={``}>
                <h1>Skills</h1>
                <div className="top">
                    <InputComposeStyled>
                        <label>Skill</label>
                        <InputSimpleStyled  type="text"/>
                    </InputComposeStyled>
                    <InputComposeStyled>
                        <label>Domain</label>
                        <InputSimpleStyled  type="text"/>
                    </InputComposeStyled>
                </div>
                <div className="bottom">
                    <textarea placeholder="description"></textarea>
                    <button className="btn" type="submit">add</button>
                </div>
                
                <div className="skills-list">
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
            </form>

            <form method="post" onSubmit={`|`} className="experiences">
                <h1>Experiences</h1>
                <div className="top">
                    <div className="left">
                        <InputComposeStyled>
                            <label>Title</label>
                            <InputSimpleStyled  type="text"/>
                        </InputComposeStyled>
                        <textarea placeholder="description"></textarea>
                    </div>
                    <div className="right">
                        <InputComposeStyled>
                            <label>Institution</label>
                            <InputSimpleStyled  type="text"/>
                        </InputComposeStyled>
                        <InputComposeStyled>
                            <label>Start Year</label>
                            <InputSimpleStyled  type="year"/>
                        </InputComposeStyled>
                        <InputComposeStyled>
                            <label>End Year</label>
                            <InputSimpleStyled  type="year"/>
                        </InputComposeStyled>
                    </div>
                </div>
                <div className="bottom">
                    <button className="btn" type="submit">add</button>
                </div>

                <div className="experiences-list">
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
            </form>

            <form method="post" onSubmit={`|`} className="certifs">
                
            </form>

            <form method="post" onSubmit={`|`} className="awards">
                
            </form>

            <form method="post" onSubmit={`|`} className="social">
                
            </form>

            <form method="post" onSubmit={`|`} className="password">
                
            </form>

            <form method="post" onSubmit={`|`} className="dbfactor">
                
            </form>

        </div>
    )
}
