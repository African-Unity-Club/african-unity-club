import Institut from '../../assets/asc.svg';
import { PencilSquare, Trash } from 'react-bootstrap-icons';

import './index.css';


export const Exp = ({ exp }) => {
    return (
        <div className="exp">
            <div className='body'>
                <div className="left">
                    <div className="top">
                        <span className="title">{exp.title}</span>
                        <small className="years">{exp.startYear} - {exp.endYear}</small>
                    </div>
                    <p className="description">{exp.description}</p>
                </div>
                <div className="right">
                    <span className="institution">{exp.institution}</span>
                    <img className="institution-logo" src={exp.institutionLogo || Institut} alt="institution logo" />
                </div>
            </div>
            <div className="bt">
                <button className="btn" type="button">
                    <PencilSquare size={16}/>
                </button>
                <button className="btn" type="button">
                    <Trash size={16}/>
                </button>
            </div>
        </div>
    );
}
