const friendlyCron = require('friendly-cron');

// Ensure correct usage
if (process.argv.length !== 3) {
    console.error(process.argv);
    console.error("Usage: node friendlycron.js '<natural language expression>'");
    process.exit(1);
}

// Get the natural language expression from the arguments
const naturalLanguageExpression = process.argv[2];

try {
    // Convert the natural language expression to a cron expression
    const cronPattern = friendlyCron(naturalLanguageExpression);
    console.log(`Cron expression: ${cronPattern}`);
} catch (error) {
    console.error('Error:', error.message);
    process.exit(1);
}
