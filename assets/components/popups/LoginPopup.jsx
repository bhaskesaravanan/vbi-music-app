import React, {useState} from 'react';
import { Modal, Button, Divider, Form, Grid, Segment } from 'semantic-ui-react';

function LoginPopup(props) {
    const [loginUserName, setLoginName] = useState("")
    const [loginPassword, setLoginPassword] = useState("")
    const [signupInfo, setSignupInfo] = useState({
        signupUserName: '',
        signupPassword: '',
        signupRePswd: ''
    });
    const [showError, setError] = useState('');

    function onChangeSignup(e, type) {
        let info = {...signupInfo};
        if(type==='userName') {
            info.signupUserName = e.target.value; 
        }
        else if(type==='password'){
            info.signupPassword = e.target.value;
        }
        else {
            info.signupRePswd = e.target.value
        }
        setSignupInfo(info);
        setError('');
    }

    function signup() {
        let {
            loginUserName,
            signupPassword,
            signupRePswd,
        } = signupInfo;

        if(!signupUserName&&!signupPassword) {
            setError('userName')
            return
        }
        else if(signupUserName && signupPassword !== signupRePswd){
            setError('retypePassword')
            return
        }
        else if(signupUserName&&!signupPassword){
            setError('password')
            return
        }
        props.signupProcess({
            userName: signupUserName,
            password: signupPassword
        });
    }

    function login() {
        props.login({
            userName: signupUserName,
            password: loginPassword
        });
    }

    return (
        <Modal
            size={'tiny'}
            open={props.loginPopup}
            onClose={() => props.showLoginPppup(false)}
        >
            <Segment placeholder>
                <Grid columns={2} relaxed='very' stackable>
                <Grid.Column>
                    <Form>
                    <Form.Input
                        icon='user'
                        iconPosition='left'
                        label='Username'
                        placeholder='Username'
                        value={loginUserName}
                        onChange={(e)=>setLoginName(e.target.value)}
                        onBlur
                    />
                    <Form.Input
                        icon='lock'
                        iconPosition='left'
                        label='Password'
                        type='password'
                        value={loginPassword}
                        onChange={(e)=>setLoginPassword(e.target.value)}
                    />

                    <Button content='Login' primary  onClick={()=>login()}/>
                    </Form>
                </Grid.Column>

                <Grid.Column verticalAlign='middle'>
                <Form>
                    <Form.Input
                        icon='user'
                        iconPosition='left'
                        label='Username'
                        placeholder='Username'
                        value={signupInfo.signupUserName}
                        onChange={(e)=>onChangeSignup(e, 'userName')}
                        error={showError==='userName'}
                    />
                    <Form.Input
                        icon='lock'
                        iconPosition='left'
                        label='Password'
                        type='password'
                        value={signupInfo.signupPassword}
                        onChange={(e)=>onChangeSignup(e, 'password')}
                        error={showError==='password'}

                    />
                    <Form.Input
                        icon='lock'
                        iconPosition='left'
                        label='Retype-Password'
                        type='password'
                        value={signupInfo.signupRePswd}
                        onChange={(e)=>onChangeSignup(e,'retypePassword')}
                        error={showError==='retypePassword'}
                    />

                    <Button content='SignUp' primary onClick={()=>signup()}/>
                    </Form>
                </Grid.Column>
                </Grid>

                <Divider vertical>Or</Divider>
            </Segment>
        </Modal>
    )
}

export default LoginPopup
