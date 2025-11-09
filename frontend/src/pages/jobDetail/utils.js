/**
 * Deeply compares two objects to check if they are identical.
 *
 * @param {object} obj1 The first object to compare.
 * @param {object} obj2 The second object to compare.
 * @returns {boolean} True if the objects are identical, otherwise false.
 */
function areObjectsEqual(obj1, obj2) {
    // Check for null or non-object types
    if (obj1 === null || typeof obj1 !== 'object' || obj2 === null || typeof obj2 !== 'object') {
        return obj1 === obj2;
    }

    // Get the keys of both objects
    const keys1 = Object.keys(obj1);
    const keys2 = Object.keys(obj2);

    // Check if they have the same number of keys
    if (keys1.length !== keys2.length) {
        return false;
    }

    // Iterate through the keys and compare values
    for (const key of keys1) {
        if (!keys2.includes(key) || !areObjectsEqual(obj1[key], obj2[key])) {
            return false;
        }
    }

    return true;
}

/**
 * Removes a specific object from an array nested within a parent object's 'json_value' property.
 * This function performs a deep comparison of all properties to find a match.
 *
 * @param {object} parentObject The parent object with the 'json_value' property.
 * @param {object} objectToRemove The object to be removed, based on a deep match.
 * @returns {object} The parent object with the specified object removed.
 */
function removeObjectWithDeepCompare(parentObject, objectToRemove) {
    const jsonValues = parentObject.json_value;

    if (jsonValues && typeof jsonValues === 'object') {
        Object.keys(jsonValues).forEach(key => {
            if (Array.isArray(jsonValues[key])) {
                // Filter the array, keeping items that are NOT a deep match to the objectToRemove.
                jsonValues[key] = jsonValues[key].filter(
                    item => !areObjectsEqual(item, objectToRemove)
                );
            }
        });
    }

    return parentObject;
}

export { removeObjectWithDeepCompare }