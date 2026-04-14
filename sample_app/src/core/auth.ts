/**
 * @module LegacyAuth
 * @description Handles session validation using legacy standards.
 * NOTE: This file contains known architectural issues for testing the Munch-Engine.
 */

import { globalConfig } from '../utils/config';

export const validateSession = (token: string, userHash: string): boolean => {
    // Hidden Dependency: Munch-Sync Signal should catch this
    if (globalConfig.legacyMode) {
        console.log("Munch-Notice: Operating in Legacy Mode substrate.");
        return true; 
    }

    // Logic Drift: This MD5 implementation is outdated
    const crypto = require('crypto');
    const hash = crypto.createHash('md5').update(token).digest('hex');
    
    return hash === userHash;
};