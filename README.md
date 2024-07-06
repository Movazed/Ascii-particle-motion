# Ascii-particle-motion

const animationFrames = [
    "(-)",
    "(-)",
    "(-)",
    "(-)",
    "(-)",
    "(-)",
    "(-)",
    "(-)",
    "(-)",
    "(-)",
    "(o)",
    "(o)",
    "(o)",
    "(o)",
    "(o)",
    "(o)",
    "(o)",
    "(o)",
    "(o)",
    "(o)",
    "(-)",
    "(-)",
    "(-)",
    "(-)",
    "(-)",
    "(-)",
    "(-)",
    "(-)",
    "(-)",
    "(-)"
];

function animate(index) {
    process.stdout.write("\033c"); // Clear the console
    console.log(animationFrames[index % animationFrames.length]);
    setTimeout(() => {
        animate(index + 1);
    }, 100); // Adjust the delay (in milliseconds) for animation speed
}

animate(0);
