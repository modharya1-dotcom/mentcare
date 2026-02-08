import React, { useState } from 'react';
import { useNavigate, useSearchParams } from 'react-router-dom';
import { Mail, Lock, ArrowRight, UserPlus, ArrowLeft } from 'lucide-react';


const SignUp = () => {
    const navigate = useNavigate();
    const [searchParams] = useSearchParams();
    const role = searchParams.get('role') || 'Patient';

    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleSignUp = (e) => {
        e.preventDefault();
        const users = JSON.parse(localStorage.getItem('users') || '{}');

        if (users[email]) {
            alert('User already exists! Please use a different email or sign in.');
            return;
        }

        users[email] = { password, role };
        localStorage.setItem('users', JSON.stringify(users));
        alert('Account created! Let\'s sign in.');
        navigate('/login');
    };

    return (
        <div style={{
            position: 'relative',
            width: '100vw',
            height: '100vh',
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            overflow: 'hidden'
        }}>


            <button
                onClick={() => navigate('/')}
                style={{
                    position: 'absolute',
                    top: '40px',
                    left: '40px',
                    color: 'var(--primary)',
                    background: 'transparent',
                    fontWeight: 700,
                    zIndex: 20,
                    display: 'flex',
                    alignItems: 'center',
                    gap: '10px',
                    border: 'none',
                    cursor: 'pointer'
                }}
            >
                <ArrowLeft size={20} /> Back to Home
            </button>

            <div className="animate-fade-in" style={{
                background: 'rgba(255, 255, 255, 0.95)',
                padding: '50px 40px',
                borderRadius: '32px',
                boxShadow: 'var(--shadow-lg)',
                width: '100%',
                maxWidth: '440px',
                display: 'flex',
                flexDirection: 'column',
                gap: '25px',
                zIndex: 10,
                border: '1px solid white'
            }}>
                <div style={{ textAlign: 'center' }}>
                    <h2 style={{ fontSize: '3.5rem', fontWeight: 900, color: 'var(--primary)', marginBottom: '10px' }}>Join Syncare</h2>
                    <p style={{ color: 'var(--text-muted)' }}>
                        Joining as a <span style={{ fontWeight: 800, color: 'var(--primary-light)' }}>{role}</span>
                    </p>
                </div>

                <form onSubmit={handleSignUp} style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
                    <div style={{ position: 'relative' }}>
                        <Mail size={20} style={{ position: 'absolute', left: '15px', top: '50%', transform: 'translateY(-50%)', color: 'var(--text-muted)' }} />
                        <input
                            type="email"
                            placeholder="Email Address"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            style={{
                                width: '100%',
                                padding: '14px 15px 14px 45px',
                                borderRadius: '16px',
                                border: '1px solid #E0E0E0',
                                fontSize: '1rem',
                                outline: 'none',
                                background: '#F9F9F9',
                                transition: 'var(--transition)'
                            }}
                            onFocus={(e) => e.target.style.borderColor = 'var(--primary)'}
                            onBlur={(e) => e.target.style.borderColor = '#E0E0E0'}
                            required
                        />
                    </div>

                    <div style={{ position: 'relative' }}>
                        <Lock size={20} style={{ position: 'absolute', left: '15px', top: '50%', transform: 'translateY(-50%)', color: 'var(--text-muted)' }} />
                        <input
                            type="password"
                            placeholder="Create Password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            style={{
                                width: '100%',
                                padding: '14px 15px 14px 45px',
                                borderRadius: '16px',
                                border: '1px solid #E0E0E0',
                                fontSize: '1rem',
                                outline: 'none',
                                background: '#F9F9F9',
                                transition: 'var(--transition)'
                            }}
                            onFocus={(e) => e.target.style.borderColor = 'var(--primary)'}
                            onBlur={(e) => e.target.style.borderColor = '#E0E0E0'}
                            required
                        />
                    </div>

                    <button
                        type="submit"
                        style={{
                            padding: '16px',
                            borderRadius: '16px',
                            border: 'none',
                            background: 'var(--primary)',
                            color: 'var(--white)',
                            fontSize: '1.1rem',
                            fontWeight: 700,
                            marginTop: '10px',
                            display: 'flex',
                            justifyContent: 'center',
                            alignItems: 'center',
                            gap: '12px',
                            boxShadow: '0 8px 20px rgba(58, 90, 120, 0.2)'
                        }}
                    >
                        Create Account
                        <UserPlus size={20} />
                    </button>
                </form>

                <div style={{ textAlign: 'center', margin: '10px 0' }}>
                    <p style={{ color: 'var(--text-muted)', fontSize: '0.9rem' }}>
                        Already have an account? <span onClick={() => navigate('/login')} style={{ color: 'var(--primary)', cursor: 'pointer', fontWeight: 700 }}>Sign In</span>
                    </p>
                </div>

                <div style={{ display: 'flex', alignItems: 'center', gap: '15px', color: '#DDD' }}>
                    <div style={{ flex: 1, height: '1px', background: '#EEE' }} />
                    <span style={{ fontSize: '0.8rem', color: '#AAA' }}>OR</span>
                    <div style={{ flex: 1, height: '1px', background: '#EEE' }} />
                </div>

                <button style={{
                    padding: '14px',
                    borderRadius: '16px',
                    border: '1px solid #EEE',
                    background: '#FFF',
                    color: 'var(--text-main)',
                    fontSize: '1rem',
                    fontWeight: 600,
                    display: 'flex',
                    justifyContent: 'center',
                    alignItems: 'center',
                    gap: '12px',
                    transition: 'var(--transition)'
                }}
                    onMouseOver={(e) => e.currentTarget.style.background = '#F9F9F9'}
                    onMouseOut={(e) => e.currentTarget.style.background = '#FFF'}
                >
                    <img src="https://www.svgrepo.com/show/475656/google-color.svg" alt="Google" style={{ width: '20px' }} />
                    Sign up with Google
                </button>
            </div>
        </div>
    );
};

export default SignUp;
