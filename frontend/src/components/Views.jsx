import '../style/Views.css'
import { LinkButtuon } from './ui/Button'
import { Facebook, Instagram, Linkedin } from 'react-bootstrap-icons'
import { Link } from 'react-router-dom'


function Views() {
    
    return (
        <main className='vwh'>
            <div className='body-vwh'>
                <div id='logo'></div>
                <div className='x-larg title'>Dream Africa</div>
                <div className='container row'>
                    <Link to="/signin" className='sign-link'>Sign In</Link>
                    <Link to="/signup" className='sign-link'>Sign Up</Link>
                </div>
                <div className='container row'>
                    <a href='facebook' className='da-link'>
                        <Facebook size={30} />
                    </a>
                    <a href='instagram' className='da-link'>
                        <Instagram size={30} />
                    </a>
                    <a href='linkedin' className='da-link'>
                        <Linkedin size={30} />
                    </a>
                </div>
            </div>
        </main>
    )
}

export default Views
