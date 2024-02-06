import { PencilSquare, Trash } from 'react-bootstrap-icons';
import './index.css';



export const Skill = ({ skill }) => {

    return (
        <div className="corps">
            <div className="tp">
                <span className="tp-title">
                    <span>{skill.name}</span>
                    <small>{skill.domain}</small>
                </span>
                <p className="tp-desc">{skill.description}</p>
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
    )
}