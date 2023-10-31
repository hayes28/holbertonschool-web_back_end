// 6. Create the Job creator
import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
    phoneNumber: '4153518780',
    message: 'This is the code to verify your account',
};

// Create a job with the jobData
const job = queue.create('push_notification_code', jobData).save((err) => {
    if (!err) {
    console.log(`Notification job created: ${job.id}`);
    }
});

// Add a 'complete' listener on the job
job.on('complete', () => {
    console.log('Notification job completed');
});

// Add a 'failed' listener on the job
job.on('failed', (err) => {
    console.log('Notification job failed');
});
