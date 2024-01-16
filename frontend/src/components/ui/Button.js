
const LinkButtuon = (props) => {
    return (
        <a href={props.href} className={props.attrs}>{props.text}</a>
    )
}

const Button = (props) => {
    return (
        <button 
            className={props.attrs} 
            type={props.action}
            onClick={props.onClick}
        >
            <i className={props.icon}></i>
            {props.text}
        </button>
    )
}


export { LinkButtuon, Button }
