import './index.css'
import Anonymous from '../../assets/nouser.png'

export const Online = ({ data }) => {

    const status = data.status
    return (
        <div className={`online-standard ${data.dim}`}>
            <img src={data.img || Anonymous} alt="" className="online-img" />
            <span className="online-dot">
                <span className={`online-dot-signal ${status ? 'online' : 'unonline'}`}></span>
            </span>
        </div>
    )
}

