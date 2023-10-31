// 7. Create the Job processor

import kue from 'kue';

const queue = kue.createQueue();

// Function to send the notification
const sendNotification = (phoneNumber, message) => {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
};

// Process the job with the function
queue.process('push_notification_code', (job, done) => {
    const { phoneNumber, message } = job.data;
    sendNotification(phoneNumber, message);
    done();
});
