import './index.css'
import Anonymous from '../../assets/nouser.png'

export const Online = ({ data }) => {

    return (
        <div className={`online-standard ${data.dim}`}>
            <img src={data.img || Anonymous} alt="" className="online-img" />
            <span className="online-dot">
                <span className={`online-dot-signal ${data.status ? 'online' : 'unonline'}`}></span>
            </span>
        </div>
    )
}

