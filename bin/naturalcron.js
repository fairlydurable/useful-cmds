var getCronString = require('@darkeyedevelopers/natural-cron.js');

// Get the arguments passed from the shell script
const args = process.argv.slice(2);

// Join the arguments to form the natural language string
const naturalLanguageCron = args.join(' ');

// Convert the natural language string to a cron spec
const cronSpec = getCronString(naturalLanguageCron);

if (cronSpec) {
    console.log(`${cronSpec}`);
} else {
    console.error('Failed to generate cron spec.');
}
