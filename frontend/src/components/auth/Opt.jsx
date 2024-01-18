import '../../style/Sign.css'



function VerifyOtp() {

    return (
        <main className='vwh'>
            <div className='picture-1'>
                <div className='logo'></div>
            </div>
            <div className='verifyotp'>
                <h1 className='order-1 title'>Sign Up</h1>
                <form className='form' onSubmit={}>
                    <div className='info'>
                        Verifier vos email
                    </div>
                    <div className=''>
                        <input 
                            type="text"
                            id='otp'
                            name='otp'
                            value={}
                            onChange={}
                            required 
                        />
                    </div>
                    <button
                        type='submit'
                        className='btn btn-primary'
                    >Send OTP</button>
                </form>
            </div>
        </main>
    )
}

export default VerifyOtp
