import { InputComposeStyled } from "../../ui/InputCompose"
import { InputSimpleStyled } from "../../ui/Input";
import './index.css';
import { useParams } from "react-router-dom";
import nouser from '../../assets/nouser.png';


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
                    <div className="corps">
                        <div className="top">
                            <span>
                                <span>skill</span>
                                <small>domain</small>
                            </span>
                            <p>description</p>
                        </div>
                        <div className="bottom">
                            <button className="btn" type="button">edit</button>
                            <button className="btn" type="button">delete</button>
                        </div>
                    </div>
                </div>
            </form>

            <div className="experiences"></div>
            <div className="certifs"></div>
            <div className="awards"></div>
            <div className="social"></div>
            <div className="password"></div>
            <div className="dbfactor"></div>
        </div>
    )
}
