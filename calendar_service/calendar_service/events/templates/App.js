document.addEventListener('DOMContentLoaded', function () {
    // Create Event
    document.getElementById('createEventForm').addEventListener('submit', function (e) {
        e.preventDefault();
        const title = document.getElementById('title').value;
        const description = document.getElementById('description').value;
        const date = document.getElementById('date').value;
        const category = document.getElementById('category').value;

        const eventData = {
            title: title,
            description: description,
            date: date,
            category: category
        };

        // Call backend API to create event
        fetch('/events', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(eventData)
        })
        .then(response => response.json())
        .then(data => {
            alert('Event created successfully');
            document.getElementById('createEventForm').reset();
        })
        .catch(error => console.error('Error:', error));
    });

    // Update Event
    document.getElementById('updateEventForm').addEventListener('submit', function (e) {
        e.preventDefault();
        const eventId = document.getElementById('eventId').value;
        const title = document.getElementById('titleUpdate').value;
        const description = document.getElementById('descriptionUpdate').value;
        const date = document.getElementById('dateUpdate').value;
        const category = document.getElementById('categoryUpdate').value;

        const eventData = {
            title: title,
            description: description,
            date: date,
            category: category
        };

        // Call backend API to update event
        fetch(`/events/${eventId}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(eventData)
        })
        .then(response => response.json())
        .then(data => {
            alert('Event updated successfully');
            document.getElementById('updateEventForm').reset();
        })
        .catch(error => console.error('Error:', error));
    });

    // Delete Event
    document.getElementById('deleteEventForm').addEventListener('submit', function (e) {
        e.preventDefault();
        const eventId = document.getElementById('eventIdDelete').value;

        // Call backend API to delete event
        fetch(`/events/${eventId}`, {
            method: 'DELETE'
        })
        .then(response => response.json())
        .then(data => {
            alert('Event deleted successfully');
            document.getElementById('deleteEventForm').reset();
        })
        .catch(error => console.error('Error:', error));
    });

    // List Events
    document.getElementById('listEventsButton').addEventListener('click', function () {
        // Call backend API to list events
        fetch('/events')
        .then(response => response.json())
        .then(data => {
            const eventsList = document.getElementById('eventsList');
            eventsList.innerHTML = '';
            data.forEach(event => {
                const eventItem = document.createElement('div');
                eventItem.textContent = `${event.title} - ${event.date} - ${event.category}`;
                eventsList.appendChild(eventItem);
            });
        })
        .catch(error => console.error('Error:', error));
    });
});
