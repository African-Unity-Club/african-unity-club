import React from 'react';
import '../style/Views.css'
import { LinkButtuon } from './ui/Button';
import { Facebook, Instagram, Linkedin } from 'react-bootstrap-icons';



class Views extends React.Component {
    
    constructor(props) {
        super(props);
        this.state = {
            views: 0
        }
    }

    // componentDidMount() {
    //     fetch('/api/views')
    //         .then(res => res.json())
    //         .then(views => this.setState({ views }));
    // }

    render() {
        
        return (
            <main className='vwh'>
                <div className='body-vwh'>
                    <div id='logo'></div>
                    <div className='x-larg title'>Dream Africa</div>
                    <div className='container row'>
                        <LinkButtuon href='/login' attrs='btn btn-primary' text='Sign In' />
                        <LinkButtuon href='/register' attrs='btn btn-primary' text='Sign Up' />
                    </div>
                    <div className='container row'>
                        <a href='facebook' className='da-link'>
                            <Facebook 
                                size={30}
                            />
                        </a>
                        <a href='instagram' className='da-link'>
                            <Instagram 
                                size={30}
                            />
                        </a>
                        <a href='linkedin' className='da-link'>
                            <Linkedin 
                                size={30}
                            />
                        </a>
                    </div>
                </div>
            </main>
        );
    }
}

export default Views
