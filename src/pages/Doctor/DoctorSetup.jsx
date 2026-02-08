import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Camera, Save } from 'lucide-react';

const DoctorSetup = () => {
    const navigate = useNavigate();
    const [formData, setFormData] = useState({
        name: '',
        phone: '',
        age: '',
        specialization: '',
        photo: null
    });

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        // Save name to session
        const session = JSON.parse(localStorage.getItem('currentUser') || '{}');
        session.name = formData.name;
        localStorage.setItem('currentUser', JSON.stringify(session));

        // Also update the user in the 'users' list if needed
        const users = JSON.parse(localStorage.getItem('users') || '{}');
        if (session.email && users[session.email]) {
            users[session.email].name = formData.name;
            localStorage.setItem('users', JSON.stringify(users));
        }

        navigate('/doctor/dashboard');
    };

    return (
        <div style={{
            width: '100vw',
            minHeight: '100vh',
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            background: '#C1AE8F', // Doctor theme
            fontFamily: 'var(--font-family)',
            padding: '20px'
        }}>
            <div style={{
                background: '#fff',
                padding: '40px',
                borderRadius: '20px',
                boxShadow: '0 10px 25px rgba(0,0,0,0.1)',
                width: '100%',
                maxWidth: '500px',
                display: 'flex',
                flexDirection: 'column',
                gap: '20px'
            }}>
                <h2 style={{ textAlign: 'center', color: '#333' }}>Complete Your Profile</h2>

                <div style={{
                    width: '100px',
                    height: '100px',
                    borderRadius: '50%',
                    background: '#f0f0f0',
                    alignSelf: 'center',
                    display: 'flex',
                    justifyContent: 'center',
                    alignItems: 'center',
                    cursor: 'pointer',
                    position: 'relative'
                }}>
                    <Camera size={40} color="#999" />
                    <div style={{ position: 'absolute', bottom: 0, right: 0, background: '#84DCC6', borderRadius: '50%', padding: '5px' }}>
                        <div style={{ width: '10px', height: '10px', background: 'white', borderRadius: '50%' }}></div>
                    </div>
                </div>

                <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>

                    <div style={{ display: 'flex', flexDirection: 'column', gap: '5px' }}>
                        <label style={{ fontSize: '0.9rem', color: '#666' }}>Full Name</label>
                        <input
                            name="name"
                            type="text"
                            placeholder="Dr. John Smith"
                            value={formData.name}
                            onChange={handleChange}
                            style={{ padding: '12px', borderRadius: '10px', border: '1px solid #ddd', outline: 'none' }}
                            required
                        />
                    </div>

                    <div style={{ display: 'flex', flexDirection: 'column', gap: '5px' }}>
                        <label style={{ fontSize: '0.9rem', color: '#666' }}>Phone Number</label>
                        <input
                            name="phone"
                            type="tel"
                            placeholder="+1 234 567 890"
                            value={formData.phone}
                            onChange={handleChange}
                            style={{ padding: '12px', borderRadius: '10px', border: '1px solid #ddd', outline: 'none' }}
                            required
                        />
                    </div>

                    <div style={{ display: 'flex', flexDirection: 'column', gap: '5px' }}>
                        <label style={{ fontSize: '0.9rem', color: '#666' }}>Age</label>
                        <input
                            name="age"
                            type="number"
                            placeholder="Years"
                            value={formData.age}
                            onChange={handleChange}
                            style={{ padding: '12px', borderRadius: '10px', border: '1px solid #ddd', outline: 'none' }}
                            required
                        />
                    </div>

                    <div style={{ display: 'flex', flexDirection: 'column', gap: '5px' }}>
                        <label style={{ fontSize: '0.9rem', color: '#666' }}>Specialization</label>
                        <input
                            name="specialization"
                            type="text"
                            placeholder="e.g. Neurologist"
                            value={formData.specialization}
                            onChange={handleChange}
                            style={{ padding: '12px', borderRadius: '10px', border: '1px solid #ddd', outline: 'none' }}
                        />
                    </div>

                    <button
                        type="submit"
                        style={{
                            padding: '15px',
                            borderRadius: '10px',
                            border: 'none',
                            background: '#333',
                            color: '#fff',
                            fontSize: '1.1rem',
                            fontWeight: 'bold',
                            marginTop: '10px',
                            display: 'flex',
                            justifyContent: 'center',
                            alignItems: 'center',
                            gap: '10px'
                        }}
                    >
                        <Save size={20} />
                        Save & Continue
                    </button>
                </form>
            </div>
        </div>
    );
};

export default DoctorSetup;
