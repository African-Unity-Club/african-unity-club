import React from 'react';
import '../style/Sign.css'



class SignUp extends React.Component {
        
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
                <div className='picture-1'>
                    <div className='logo'></div>
                </div>
                <div className='signup'>
                    <h1 className='order-1 title'>Sign Up</h1>
                    <form className='form'>
                        <div className='form-group'>
                            <label for='username'>Username</label>
                            <input type='text' className='form-control' id='username' placeholder='Enter username' required/>
                            <span className='error-message'></span>
                        </div>
                        <div className='form-group'>
                            <label for='email'>Email</label>
                            <input type='email' className='form-control' id='email' placeholder='Enter email' required/>
                            <span className='error-message'></span>
                        </div>
                        <div className='form-group'>
                            <label for='password'>Password</label>
                            <input type='password' className='form-control' id='password' placeholder='Enter password' required/>
                            <span className='error-message'></span>
                        </div>
                        <div className='form-group'>
                            <label for='password2'>Confirm Password</label>
                            <input type='password' className='form-control' id='password2' placeholder='Confirm password' required/>
                            <span className='error-message'></span>
                        </div>
                        <button type='submit' className='btn btn-primary'>Sign Up</button>
                    </form>
                </div>
            </main>
        );
    }
}   