// Copyright 2019 Shift Cryptosecurity AG
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#ifndef _WORKFLOW_RESTORE_FROM_MNEMONIC_H_
#define _WORKFLOW_RESTORE_FROM_MNEMONIC_H_

#include <hww.pb.h>
#include <stdbool.h>

/**
 * Enter a 12/18/24 word mnemonic and set the keystore seed from it.
 * @return true on success, false on abort or failure.
 */
bool workflow_restore_from_mnemonic(const RestoreFromMnemonicRequest* request);

#endif
