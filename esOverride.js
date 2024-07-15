// Select the node that will be observed for mutations
let targetNode = document.getElementsByClassName("x9f619 x78zum5 xdt5ytf x1odjw0f xish69e x1xzabdm xh8yej3");
let socket = new WebSocket('ws://localhost:8765');

// Options for the observer (which mutations to observe)
const config = { attributes: true, childList: true, subtree: true };

// Callback function to execute when mutations are observed
let callback = (mutationList, observer) => {
  for (const mutation of mutationList) {
    if (mutation.type === "childList" && mutation.addedNodes.length > 0) {
      console.log("A child node has been added ");
      console.log(mutation.addedNodes);
      for(added of mutation.addedNodes) {
        console.log(added);
        userName = added.getElementsByClassName("x6s0dn4 xt0psk2 x1q0g3np")[0].innerText;
        commentData = added.getElementsByClassName("x1lliihq xjkvuk6 x1iorvi4")[0].innerText;
        console.log(userName);
        console.log(commentData);
        const data = { userName, commentData };
        // Sending data to the Python server
        socket.send(JSON.stringify(data));
      }
    }
  }
};
let observer = new MutationObserver(callback);
/*
Username = x6s0dn4 xt0psk2 x1q0g3np
CommmentData = x1lliihq xjkvuk6 x1iorvi4
*/

// Start observing the target node for configured mutations
observer.observe(targetNode[0], config);

// Later, you can stop observing

// Create an observer instance linked to the callback function
observer.disconnect();
