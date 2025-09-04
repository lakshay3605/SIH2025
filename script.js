// Simple chat functionality for demonstration
document.querySelector('.chat-input button').addEventListener('click', function() {
    const input = document.querySelector('.chat-input input');
    const message = input.value.trim();
    
    if (message) {
        const chatMessages = document.querySelector('.chat-messages');
        const now = new Date();
        const time = now.getHours() + ':' + String(now.getMinutes()).padStart(2, '0');
        
        const messageElement = document.createElement('div');
        messageElement.className = 'message user-message';
        messageElement.innerHTML = `
            <p>${message}</p>
            <div class="timestamp">${time}</div>
        `;
        
        chatMessages.appendChild(messageElement);
        input.value = '';
        
        // Auto-scroll to bottom
        chatMessages.scrollTop = chatMessages.scrollHeight;
        
        // Simulate AI response after a delay
        setTimeout(function() {
            const aiResponse = document.createElement('div');
            aiResponse.className = 'message ai-message';
            aiResponse.innerHTML = `
                <p>I'm processing your request for "${message}". Here are the results visualized on the map and graphs.</p>
                <div class="timestamp">${time}</div>
            `;
            
            chatMessages.appendChild(aiResponse);
            chatMessages.scrollTop = chatMessages.scrollHeight;
            
            // Simulate data points appearing on the map
            simulateDataPoints();
            
        }, 1000);
    }
});

// Allow sending message with Enter key
document.querySelector('.chat-input input').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        document.querySelector('.chat-input button').click();
    }
});

// Make query pills clickable
document.querySelectorAll('.query-pill').forEach(pill => {
    pill.addEventListener('click', function() {
        document.querySelector('.chat-input input').value = this.textContent;
    });
});

// Add interactivity to data points
document.querySelectorAll('.data-point').forEach(point => {
    point.addEventListener('click', function() {
        // Highlight the selected point
        document.querySelectorAll('.data-point').forEach(p => {
            p.style.transform = 'translate(-50%, -50%) scale(1)';
            p.style.boxShadow = '0 0 10px rgba(255, 158, 0, 0.5)';
        });
        
        this.style.transform = 'translate(-50%, -50%) scale(1.5)';
        this.style.boxShadow = '0 0 15px 5px rgba(255, 158, 0, 0.8)';
        
        // Show a tooltip with information (simulated)
        showFloatInfo(this.style.backgroundColor);
    });
});

// Simulate data points appearing on the map
function simulateDataPoints() {
    const dataPoints = document.querySelectorAll('.data-point');
    dataPoints.forEach(point => {
        point.style.opacity = '0';
        point.style.transition = 'opacity 0.5s ease-in-out';
    });
    
    let delay = 0;
    dataPoints.forEach(point => {
        setTimeout(() => {
            point.style.opacity = '1';
        }, delay);
        delay += 200;
    });
}

// Show information about a float (simulated)
function showFloatInfo(color) {
    // In a real application, this would show actual data based on the selected float
    const messages = [
        "ARGO Float #3871: Temperature 22.4°C, Salinity 34.8 PSU",
        "ARGO Float #5298: Temperature 18.7°C, Salinity 35.2 PSU",
        "ARGO Float #6712: Temperature 25.1°C, Salinity 34.5 PSU",
        "ARGO Float #4439: Temperature 16.3°C, Salinity 35.6 PSU",
        "ARGO Float #7865: Temperature 28.9°C, Salinity 33.9 PSU"
    ];
    
    const randomMessage = messages[Math.floor(Math.random() * messages.length)];
    
    // Create a temporary notification
    const notification = document.createElement('div');
    notification.style.position = 'fixed';
    notification.style.bottom = '20px';
    notification.style.right = '20px';
    notification.style.backgroundColor = 'rgba(9, 35, 55, 0.9)';
    notification.style.color = '#90e0ef';
    notification.style.padding = '15px';
    notification.style.borderRadius = '8px';
    notification.style.boxShadow = '0 4px 12px rgba(0, 0, 0, 0.3)';
    notification.style.zIndex = '1000';
    notification.style.maxWidth = '300px';
    notification.textContent = randomMessage;
    
    document.body.appendChild(notification);
    
    // Remove the notification after 5 seconds
    setTimeout(() => {
        notification.style.opacity = '0';
        notification.style.transition = 'opacity 0.5s ease-in-out';
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 500);
    }, 5000);
}

// Initialize the interface
document.addEventListener('DOMContentLoaded', function() {
    // Simulate data points appearing when the page loads
    setTimeout(simulateDataPoints, 1000);
    
    // Add sample data points to the map
    addSampleDataPoints();
});

// Add sample data points to the map
function addSampleDataPoints() {
    const dataPointsContainer = document.querySelector('.data-points');
    
    // Clear existing points
    dataPointsContainer.innerHTML = '';
    
    // Add new points at random positions
    for (let i = 0; i < 15; i++) {
        const point = document.createElement('div');
        point.className = 'data-point';
        
        // Random position
        const top = Math.random() * 80 + 10; // 10% to 90%
        const left = Math.random() * 80 + 10; // 10% to 90%
        
        point.style.top = `${top}%`;
        point.style.left = `${left}%`;
        
        // Random color from a predefined set
        const colors = ['#ff9e00', '#48cae4', '#9d4edd', '#f72585', '#4cc9f0'];
        point.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
        
        dataPointsContainer.appendChild(point);
        
        // Add click event to each point
        point.addEventListener('click', function() {
            // Highlight the selected point
            document.querySelectorAll('.data-point').forEach(p => {
                p.style.transform = 'translate(-50%, -50%) scale(1)';
                p.style.boxShadow = '0 0 10px rgba(255, 158, 0, 0.5)';
            });
            
            this.style.transform = 'translate(-50%, -50%) scale(1.5)';
            this.style.boxShadow = '0 0 15px 5px rgba(255, 158, 0, 0.8)';
            
            // Show a tooltip with information (simulated)
            showFloatInfo(this.style.backgroundColor);
        });
    }
}