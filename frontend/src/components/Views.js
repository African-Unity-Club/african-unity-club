import react from 'react';
import '../style/Views.css'
import { LinkButtuon, IconLinkButton } from './ui/Button';


class Views extends react.Component {
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
                        <IconLinkButton href='/facebook link' attrs='link icon' icon='fab fa-facebook-f' />
                        <IconLinkButton href='/instagram link' attrs='link icon' icon='fab fa-facebook-f' />
                    </div>
                </div>
            </main>
        );
    }
}

export default Views
