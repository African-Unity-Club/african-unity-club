import '../../style/Sign.css'
import { useState, useEffect } from 'react';



function VerifyOtp() {

    const [otp, setOtp] = useState('');

    // verification de l'otp une fois la valeur de otp est a 6
    useEffect(() => {
        if (otp.length === 6) {
            handleSubmmit();
        }
    }, [otp]);

    const handleSubmmit = (e) => {

        //const token = redis.get(params.email)
            // if (token.otp === otp) {
            //     if (token.expired > Date.now()) {
            //         // sauvegarder les données dans la base de données mongo
            //         // mongo.save(params.username, params.email, params.password)
            //     } else {
            //         document.getElementById('otp').nextSibling.innerHTML = 'OTP expired';
            //     }
            // } else {
            //     document.getElementById('otp').nextSibling.innerHTML = 'OTP invalid';
            // }
    }

    return (
        <main className='vwh sign verify'>
            <div className='verifyotp'>
                <h1 className='order-1 title'>Email verify</h1>
                <form className='form' method='post'>
                    <div className='info'>
                        Verifier vos emails
                    </div>
                    <div className='form-group'>
                        <input 
                            type="text"
                            id='otp'
                            name='otp'
                            value={otp}
                            onChange={(e) => setOtp(e.target.value)}
                            required 
                        />
                        <span className='error'></span>
                    </div>
                </form>
            </div>
        </main>
    )
}

export default VerifyOtp
