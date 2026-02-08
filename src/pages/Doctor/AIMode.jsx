import React, { useEffect, useState } from 'react';
import { Calendar as CalendarIcon, MessageSquare, Mic } from 'lucide-react';
import useSpeechRecognition from '../../hooks/useSpeechRecognition';

const AIMode = () => {
    const { text, isListening, startListening, stopListening, hasSupport } = useSpeechRecognition();
    const [inputValue, setInputValue] = useState('');

    useEffect(() => {
        if (text) {
            setInputValue(text);
        }
    }, [text]);

    return (
        <div style={{ height: '100%', display: 'flex', gap: '20px' }}>

            {/* Left Panel: Calendar & Insights List */}
            <div style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: '20px' }}>
                <div style={{ background: '#fff', padding: '20px', borderRadius: '20px', flex: 1 }}>
                    <h3 style={{ marginBottom: '15px', display: 'flex', alignItems: 'center', gap: '10px' }}>
                        <CalendarIcon size={20} /> Daily Monitoring
                    </h3>
                    <div style={{ border: '1px dashed #ccc', padding: '20px', borderRadius: '10px', height: '200px', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#999' }}>
                        Calendar Viz Placeholder
                    </div>
                </div>

                <div style={{ background: '#fff', padding: '20px', borderRadius: '20px', flex: 1 }}>
                    <h3 style={{ marginBottom: '15px' }}>Today's Insights</h3>
                    <div style={{ fontSize: '0.9rem', color: '#444', lineHeight: '1.5' }}>
                        • Patient showed signs of confusion around 10:00 AM.<br />
                        • Mood improved after lunch.<br />
                        • Sleeping patterns were irregular last night.
                    </div>
                </div>
            </div>

            {/* Right Panel: AI Chat */}
            <div style={{ flex: 1, background: '#fff', borderRadius: '20px', padding: '20px', display: 'flex', flexDirection: 'column' }}>
                <div style={{ borderBottom: '1px solid #eee', paddingBottom: '15px', marginBottom: '15px', display: 'flex', justifyContent: 'space-between' }}>
                    <h3>AI Assistant</h3>
                    <button
                        onClick={() => isListening ? stopListening() : startListening()}
                        style={{
                            background: isListening ? '#ff4d4d' : '#84DCC6',
                            color: '#fff',
                            padding: '5px 10px',
                            borderRadius: '10px',
                            fontSize: '0.8rem',
                            display: 'flex',
                            alignItems: 'center',
                            gap: '5px',
                            border: 'none',
                            cursor: 'pointer',
                            transition: 'background 0.3s'
                        }}
                    >
                        <Mic size={12} /> {isListening ? 'Stop Listening' : 'Tap to Speak'}
                    </button>
                </div>

                <div style={{ flex: 1, background: '#f9f9f9', borderRadius: '10px', padding: '15px', marginBottom: '15px', overflowY: 'auto' }}>
                    <div style={{ marginBottom: '10px', alignSelf: 'flex-start', background: '#e0e0e0', padding: '10px', borderRadius: '10px 10px 10px 0', maxWidth: '80%' }}>
                        Hello Dr. Smith. I've compiled the daily report for John Doe.
                    </div>
                </div>

                <div style={{ display: 'flex', gap: '10px' }}>
                    <input
                        type="text"
                        placeholder={isListening ? "Listening..." : "Ask the AI about the patient..."}
                        value={inputValue}
                        onChange={(e) => setInputValue(e.target.value)}
                        style={{ flex: 1, padding: '10px', borderRadius: '10px', border: '1px solid #ddd', outline: 'none' }}
                    />
                    <button style={{ background: '#333', color: '#fff', border: 'none', borderRadius: '10px', padding: '10px', cursor: 'pointer' }}>
                        <MessageSquare size={20} />
                    </button>
                </div>
            </div>

        </div>
    );
};

export default AIMode;
